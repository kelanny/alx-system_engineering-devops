
# Postmortem: The Great Checkout Crash of 2024
by **Kelvin Chuchu**
**Published**: 6, June 2024

Read article on  [medium](https://medium.com/@mburukelvin17/an-incident-report-on-the-great-e-commerce-checkout-crash-2024-e3ea17ef080d)

### A Comic Relief

Picture this: It's a typical Tuesday afternoon when suddenly, the e-commerce world falls into chaos. A single server, burdened with the hopes and dreams of countless shoppers, throws in the towel. Chaos ensues, engineers scramble, and the checkout button becomes the most dreaded feature on the site. Here's a light-hearted look at how a simple misconfiguration can bring a bustling online store to a halt and the heroic journey to fix it.

While we can laugh about it now, this incident reminded us of the importance of vigilance in configuration management. Thanks for sticking with us through this roller-coaster!

### Issue Summary

- **Duration of the Outage**: March 3, 2024, 14:30 - 16:00 GMT
- **Impact**: The checkout service on our e-commerce website was down. Users were unable to complete purchases, resulting in a 90% drop in transaction volume during the outage. Approximately 60% of our active users were affected.
- **Root Cause**: A misconfiguration in the load balancer settings caused an overload on a single server, leading to a failure in the checkout process.

### Timeline

- **14:30**: Issue detected through a monitoring alert indicating a spike in checkout failures.
- **14:32**: On-call engineer confirmed the issue by replicating the checkout process failure.
- **14:35**: Initial investigation focused on the payment gateway API, suspecting an external service issue.
- **14:45**: Further investigation showed that the payment gateway was functioning correctly.
- **14:50**: The issue was escalated to the backend engineering team.
- **15:00**: Misleading path explored by inspecting database performance, which was found to be normal.
- **15:15**: Realized the issue might be related to server load distribution.
- **15:20**: Load balancer logs inspected, revealing a misconfiguration.
- **15:30**: Configuration corrected and load balancer reloaded.
- **15:45**: Checkout service gradually restored as server loads normalized.
- **16:00**: Full functionality confirmed, and the incident was marked as resolved.

### Root Cause and Resolution

- **Root Cause**: The load balancer was incorrectly configured to route all checkout traffic to a single server instead of distributing it evenly across the server pool. This caused the designated server to become overloaded, leading to failures in processing checkout requests.
- **Resolution**: The load balancer configuration was corrected to ensure even traffic distribution across all servers. The load balancer was then reloaded to apply the new configuration, and server performance was monitored to ensure stability.

### Corrective and Preventative Measures

- **Improvements/Fixes**:
    
    - Improve load balancer configuration management to prevent misconfigurations.
    - Enhance monitoring to detect uneven traffic distribution and server overloads more quickly.
    - Implement automated load balancer configuration validation tools.
- **Tasks to Address the Issue**:
    
    1. **Patch Load Balancer Configuration**: Review and update load balancer settings to ensure proper traffic distribution.
    2. **Add Monitoring on Server Load**: Implement detailed monitoring for server load and traffic distribution to detect anomalies early.
    3. **Automate Configuration Checks**: Develop and deploy scripts to automatically validate load balancer configurations upon changes.
    4. **Conduct Training**: Provide training for engineering and operations teams on load balancer management and monitoring best practices.
    5. **Review Incident Response Protocols**: Update incident response procedures to include specific steps for diagnosing and resolving load balancer issues.

By addressing these areas, we aim to prevent similar incidents in the future and enhance the overall reliability and resilience of our e-commerce platform.
