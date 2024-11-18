import time
import logging
import argparse
import sys
import signal
import psutil

class SystemMonitor:
    def __init__(self, interval=10, duration=None):
        """
        Initialize the SystemMonitor.
        
        Args:
            interval (int): Monitoring interval in seconds (default: 10)
            duration (int): Total monitoring duration in seconds (default: None, runs indefinitely)
        """
        self.interval = interval
        self.duration = duration
        self.start_time = time.time()
        self.setup_logging()
        self.setup_signal_handlers()
        
    def setup_logging(self):
        """Configure logging settings"""
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - CPU Load: %(cpu_load)s - Memory Used: %(memory_used)s%%',
            datefmt='%Y-%m-%d %H:%M:%S',
            handlers=[
                logging.FileHandler('system_monitor.log'),
                logging.StreamHandler(sys.stdout)
            ]
        )
        self.logger = logging.getLogger(__name__)
        
    def setup_signal_handlers(self):
        """Setup handlers for graceful shutdown"""
        signal.signal(signal.SIGINT, self.handle_shutdown)
        signal.signal(signal.SIGTERM, self.handle_shutdown)
        
    def handle_shutdown(self, signum, frame):
        """Handle shutdown signals gracefully"""
        print("\nShutting down system monitor...")
        sys.exit(0)
        
    def get_cpu_load(self):
        """Get current CPU load percentage"""
        try:
            cpu_load = psutil.cpu_percent(interval=None)  # Get immediate CPU usage
            return f"{cpu_load}%"
        except Exception as e:
            return f"Unable to get CPU load: {e}"
            
    def get_memory_usage(self):
        """Get memory usage percentage"""
        try:
            memory = psutil.virtual_memory()  # Get memory usage
            return f"{memory.percent}%"
        except Exception as e:
            return f"Unable to get memory usage: {e}"
        
    def log_metrics(self):
        """Log current system metrics"""
        cpu_load = self.get_cpu_load()
        memory_used = self.get_memory_usage()
        self.logger.info(
            '',
            extra={
                'cpu_load': cpu_load,
                'memory_used': memory_used
            }
        )
        
    def should_continue(self):
        """Check if monitoring should continue based on duration"""
        if self.duration is None:
            return True
        return (time.time() - self.start_time) < self.duration
        
    def run(self):
        """Main monitoring loop"""
        print(f"Starting system monitoring (Interval: {self.interval}s, Duration: {self.duration if self.duration else 'indefinite'})")
        print("Press Ctrl+C to stop monitoring...")
        
        try:
            while self.should_continue():
                self.log_metrics()
                time.sleep(self.interval)
                
        except KeyboardInterrupt:
            print("\nMonitoring stopped by user")
        except Exception as e:
            print(f"\nError occurred: {e}")
        finally:
            print("\nMonitoring ended")

def parse_arguments():
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(description='Monitor system CPU and memory usage')
    parser.add_argument(
        '-i', '--interval',
        type=int,
        default=10,
        help='Monitoring interval in seconds (default: 10)'
    )
    parser.add_argument(
        '-d', '--duration',
        type=int,
        help='Total monitoring duration in seconds (default: run indefinitely)'
    )
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_arguments()
    monitor = SystemMonitor(interval=args.interval, duration=args.duration)
    monitor.run()