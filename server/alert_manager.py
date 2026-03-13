def check_alerts(data):

    alerts = []

    if data["cpu"] > 80:
        alerts.append("CPU usage high")

    if data["memory"] > 80:
        alerts.append("Memory usage high")

    if data["disk"] > 90:
        alerts.append("Disk usage critical")

    return alerts