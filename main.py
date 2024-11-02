from newjob_alert import microalert

Alert=microalert()

Alert.monitor_jobs(check_interval=60)