#Postmortem Report

## 503 Error while accessing a website

### Incident report

#### Summary

On May 5th, 2023, between 2:00 PM to 6:00 PM PST, our website experienced an outage resulting in a complete service disruption. Users attempting to access our website received 503 errors or were unable to connect. Approximately 90% of our users were affected. The root cause of the outage was traced to a misconfigured load balancer.

#### Timeline

- **2:00 PM** - The outage was first detected by a customer who attempted to access our website and received a 503 error. The customer reported the issue to our support team.
- **2:05 PM:** - Our support team received multiple reports of the outage and escalated the issue to the engineering team.
- **2:10 PM:** - The engineering team received an alert from our monitoring system indicating high levels of 503 errors. The team began investigating the issue, starting with the web servers.
- **2:20 PM:** - The investigation revealed that the web servers were up and running without any issues. The team then turned their attention to the load balancer.
- **2:30 PM:** - It was discovered that a recent change to the load balancer's configuration resulted in misrouting traffic to non-existent servers, leading to a bottleneck and eventual service disruption.
- **2:45 PM:** - The team attempted to roll back the configuration changes but were unsuccessful due to a bug in the load balancer software.
- **3:00 PM:** - The team contacted the vendor for support, and the incident was escalated to their engineering team.
- **3:30 PM:** - The vendor's engineering team identified the root cause of the issue as a known bug in the load balancer software.
- **4:00 PM:** - A hotfix was developed and tested by the vendor's engineering team.
- **5:00 PM:** - The hotfix was successfully deployed to our load balancer, and the website was brought back online.
- **6:00 PM:** - The website was fully functional, and the incident was declared resolved.

#### Root Cause and Resolution

The root cause of the outage was traced to a misconfigured load balancer resulting from a recent change in its configuration. The change led to misrouted traffic, causing a bottleneck and eventual service disruption. The incident was resolved by deploying a hotfix developed by the vendor to address the known bug in the load balancer software.

#### Corrective and Preventive Measures

To prevent similar incidents from occurring in the future, the following corrective and preventative measures will be taken:

  - Implement better testing and review procedures for configuration changes to critical systems.
  -  Increase redundancy by adding additional load balancers and web servers to handle traffic spikes and prevent bottlenecks.
  - Improve our monitoring and alerting systems to provide better visibility into the health of our systems and services.
  - Schedule regular reviews of our infrastructure to identify and address potential issues before they become critical. 

#### Conclusion

The outage experienced by our website on May 5th, 2023, was caused by a misconfigured load balancer resulting from a recent change in its configuration. The incident was resolved with the help of the vendor's engineering team, who developed and deployed a hotfix to address the known bug in the load balancer software. We have identified corrective and preventative measures to prevent similar incidents from occurring in the future and will be implementing them to improve the reliability and stability of our services.
