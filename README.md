# Bank API

## Overview
Bank API is a comprehensive, Django-based banking system designed to provide secure, scalable, and efficient banking services. It covers a wide range of functionalities including user authentication, account management, transaction processing, KYC verification, virtual card management, and more. The entire application is containerized using Docker and leverages modern technologies such as Celery, RabbitMQ, Redis, and Nginx to ensure robust performance and scalability.

## Key Features
- **User Authentication & Authorization**  
  - Secure sign-up, login, logout with OTP verification and JWT token management  
  - Role-based access control (Customer, Teller, Account Executive, Branch Manager)
- **Bank Account Management**  
  - Create, deposit, withdraw, and transfer funds between accounts  
  - Automated interest accrual and transaction recording
- **KYC and Profile Management**  
  - Comprehensive user profiles with KYC verification and next-of-kin information  
  - Dynamic profile completeness validation
- **Transaction History & Reporting**  
  - Detailed transaction logging and history retrieval  
  - On-demand PDF report generation for transaction histories
- **Virtual Card Management**  
  - Create and manage virtual cards linked to bank accounts  
  - Support for top-up and balance updates with email notifications
- **Email Notifications**  
  - Automated notifications for account creation, transactions, and security alerts using templated emails
- **Asynchronous Task Processing**  
  - Background processing with Celery for long-running tasks such as email delivery, PDF generation, and scheduled jobs  
  - Flower monitoring for Celery workers
- **Advanced Logging & Monitoring**  
  - Centralized logging with Loguru and custom interceptors for robust traceability
- **Containerized Deployment**  
  - Docker Compose setup to orchestrate the API, PostgreSQL, RabbitMQ, Redis, and Nginx services
  - Seamless local, staging, and production deployments

## Tech Stack
- **Backend:** Python, Django, Django REST Framework (DRF)
- **Database:** PostgreSQL
- **Message Broker:** RabbitMQ (for Celery tasks)
- **Caching:** Redis
- **Storage:** Cloudinary (for user profile images and documents)
- **Web Server:** Nginx (reverse proxy, static file serving, load balancing)
- **Containerization:** Docker, Docker Compose
- **Task Processing:** Celery, Flower
- **Logging:** Loguru

## Installation & Setup

### Prerequisites
- **Python 3.12+**
- **Pipenv** for dependency management (alternatively, use Docker for an isolated environment)
- **Docker** and **Docker Compose** (recommended for full environment consistency)


