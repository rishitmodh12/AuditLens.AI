"""
Pre-curated enterprise policy and contract documents.
Specifically crafted to demonstrate:
1. Multi-source evidence synthesis (combining facts across 2 or 3 documents).
2. Deep citations to exact sections and clauses.
3. Obvious contractual contradiction (SLA 1-hour allowed downtime vs Cloud Vendor 4-hour maintenance).
4. Guardrails against out-of-scope / unanswerable questions.
"""

SAMPLE_DOCUMENTS = [
    {
        "doc_id": "doc_customer_sla",
        "doc_name": "Customer_Enterprise_SLA_2026.pdf",
        "category": "Customer Agreement",
        "sections": [
            {
                "section": "Section 1.1: Service Availability Target",
                "text": "The Provider guarantees a monthly service availability uptime target of 99.90% for all production API endpoints. Total cumulative unscheduled downtime across any single calendar month shall not exceed 1.0 hour (60 minutes)."
            },
            {
                "section": "Section 2.4: Outage Notification Protocol",
                "text": "In the event of an unscheduled service interruption affecting production traffic, Provider must issue an official incident communication to Customer Technical Contacts within forty-five (45) minutes of incident detection."
            },
            {
                "section": "Section 4.2: Service Credit Penalties & Liability",
                "text": "If cumulative monthly downtime exceeds 1.0 hour, Customer shall be entitled to a Service Credit penalty of $1,000 USD for each full hour of downtime, up to a maximum aggregate credit of 50% of the customer's monthly recurring software fee."
            },
            {
                "section": "Section 5.3: Force Majeure & Exclusions",
                "text": "Downtime caused by customer misconfiguration, unauthorized third-party penetration testing, or sovereign national internet outages shall be excluded from SLA penalty calculations."
            }
        ]
    },
    {
        "doc_id": "doc_security_policy",
        "doc_name": "Internal_Security_Incident_Policy_v4.pdf",
        "category": "Internal Operations",
        "sections": [
            {
                "section": "Clause 3.2: Incident Severity & Escalation",
                "text": "Any unscheduled API outage affecting more than 10% of active customer sessions is automatically classified as a Severity-1 (Sev-1) incident. The Lead Site Reliability Engineer (SRE) must formally notify the VP of Engineering and Legal Counsel within thirty (30) minutes of alert confirmation."
            },
            {
                "section": "Clause 5.1: Mitigation & Patch Timelines",
                "text": "For Sev-1 vulnerabilities or software regressions causing active downtime, an emergency mitigation patch or rollback must be deployed into the production staging environment within two (2.0) hours of initial incident confirmation."
            },
            {
                "section": "Clause 7.4: Audit Logs & Evidence Preservation",
                "text": "All raw system telemetry, API request logs, audit trails, and deployment history surrounding an incident must be frozen and preserved for a minimum of 365 calendar days in write-once tamper-evident storage."
            },
            {
                "section": "Clause 8.3: Post-Mortem Obligation",
                "text": "A comprehensive Root Cause Analysis (RCA) and post-mortem report must be completed and submitted to the Chief Technology Officer (CTO) within forty-eight (48) hours of service restoration."
            }
        ]
    },
    {
        "doc_id": "doc_cloud_vendor",
        "doc_name": "Cloud_Vendor_Master_Services_Agreement.pdf",
        "category": "Vendor Contract",
        "sections": [
            {
                "section": "Article 4.1: Permitted Maintenance Windows",
                "text": "Vendor reserves the right to conduct scheduled infrastructure maintenance, kernel upgrades, and emergency hardware repairs for up to four (4.0) hours per maintenance window. Scheduled downtime within this window is permitted and incurs zero financial penalty or service credit liability."
            },
            {
                "section": "Article 6.3: Data Residency & Sovereignty",
                "text": "All primary customer databases, vector indexes, and object stores must strictly reside within the AWS Asia-Pacific Mumbai (ap-south-1) cloud region. Cross-border replication outside of India is strictly prohibited without explicit written consent."
            },
            {
                "section": "Article 8.5: Vendor Maximum Liability Cap",
                "text": "Notwithstanding any other provision, Vendor's total aggregate liability arising out of or related to service unavailability, infrastructure failures, or data corruption shall be capped at $500 USD total, regardless of the cause."
            },
            {
                "section": "Article 11.2: Dispute Resolution",
                "text": "Any contractual disputes shall be resolved through confidential expedited commercial arbitration seated in Mumbai under the rules of the Indian Council of Arbitration."
            }
        ]
    }
]
