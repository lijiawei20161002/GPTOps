from vm_price_monitoring import VMPriceMonitoringSystem

system = VMPriceMonitoringSystem(data_path='../tasks/dynamic vm pricing/data series/aws/combined_spot_prices.txt')
system.run_cycle()