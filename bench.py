import argparse
import requests
import time
import sys

def run_bench(hosts, count):
    host_list = hosts.split(',')
    
    for host in host_list:
        host = host.strip()
        print(f"\n--- Testing host: {host} ({count} requests) ---")
        
        stats = {
            'success': 0,
            'failed': 0,
            'errors': 0,
            'times': []
        }

        for i in range(count):
            try:
                start_time = time.perf_counter()
                
                response = requests.get(host, timeout=10)
                end_time = time.perf_counter()
                
                duration = (end_time - start_time) * 1000  
                stats['times'].append(duration)

                if 200 <= response.status_code < 400:
                    stats['success'] += 1
                else:
                    stats['failed'] += 1
                    
            except requests.exceptions.RequestException as e:
                stats['errors'] += 1
            
        display_stats(host, stats)

def display_stats(host, stats):
    if stats['times']:
        min_t = f"{min(stats['times']):.2f}ms"
        max_t = f"{max(stats['times']):.2f}ms"
        avg_t = f"{(sum(stats['times']) / len(stats['times'])):.2f}ms"
    else:
        min_t = max_t = avg_t = "N/A"

    print(f"{'Host:':<10} {host}")
    print(f"{'Success:':<10} {stats['success']}")
    print(f"{'Failed:':<10} {stats['failed']}")
    print(f"{'Errors:':<10} {stats['errors']}")
    print(f"{'Min:':<10} {min_t}")
    print(f"{'Max:':<10} {max_t}")
    print(f"{'Avg:':<10} {avg_t}")
    print("-" * (20 + len(host)))

def main():
    parser = argparse.ArgumentParser(description="HTTP Availability Benchmark Tool")
    
    parser.add_argument("-H", "--hosts", required=True, 
                        help="Comma-separated list of hosts (e.g., https://ya.ru,https://google.com)")
    parser.add_argument("-C", "--count", type=int, default=1, 
                        help="Number of requests per host (default: 1)")

    args = parser.parse_args()

    try:
        run_bench(args.hosts, args.count)
    except KeyboardInterrupt:
        print("\n\nTesting interrupted by user.")
        sys.exit(0)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()