# Airflow Docker-in-Docker Project

# Table of Contents
- [Introduction](#introduction)
- [Motivation](#motivation---why-use-docker-in-docker-dind)
- [Getting Started](#getting-started)
- [Install Requirements](#install-requirements)
- [Setup DinD](#setup-dind)
- [Run Dags](#run-dags)
- [Security](#security)
- [Acknowledgments](#acknowledgments)


# Introduction
This project provides a comprehensive guide and setup for running Apache Airflow within a Docker-in-Docker (DinD) environment. It is designed to help users understand how to deploy and manage Airflow using Docker containers, and then leverage Docker operations within Airflow itself.

By the end of this project, you'll have a fully functional Airflow setup running inside Docker, with the capability to perform Docker operations directly from your Airflow tasks. This is an ideal setup for those looking to automate complex workflows that involve managing containerized applications or services.

# Motivation - Why Use Docker-in-Docker (DinD)?
When it comes to running tasks within data pipelines or automated workflows, there are several approaches you can take. You might run tasks directly on the host system, use virtual machines for isolated environments, or leverage traditional containerization methods. Each of these options has its own set of benefits and limitations. However, when your tasks require the flexibility to manage and operate Docker containers themselves, the Docker-in-Docker (DinD) approach offers distinct advantages.

Docker-in-Docker combines the lightweight nature of containers with the ability to manage Docker operations directly within your tasks. This is particularly beneficial when your workflows involve creating, running, or managing Docker containers as part of their execution. DinD allows for this without requiring elevated permissions on the host system or setting up complex virtual machine infrastructures.

By using DinD, each task is encapsulated within its own Docker container, running in an isolated environment. This prevents conflicts and interference between tasks, ensuring that dependencies and operations remain contained. This isolation is crucial for maintaining clean, repeatable, and conflict-free environments, especially in complex or multi-user systems.

[Read more here](https://medium.com/@shivam77kushwah/docker-inside-docker-e0483c51cc2c#:~:text=Running%20Docker%20inside%20Docker%20allows,2.)

# Install Requirements

Before we dive into setting up Docker-in-Docker (DinD) with Airflow, you'll need to ensure that both Docker and Airflow are installed on your system. If you've already installed them, feel free to skip ahead to the next section.

## 1. Install Docker
First, you'll need to install Docker. The best resource for this is the official Docker documentation. Alternatively, you can install Docker Desktop, which provides both Docker Engine and Docker Compose, so you won't need any additional tools. Docker Desktop is available for Windows, macOS, and Linux.

## 2. Install Airflow
Once Docker is installed, you'll need to set up Airflow. Begin by creating a directory for your Airflow setup. This directory will house your Docker Compose YAML file and any required subdirectories.

### Recommended Directory Structure
It's a good practice to first create the main directory, then download the Docker Compose YAML file into this directory, and finally, create any required subdirectories as specified in the YAML file.

You can find a straightforward guide for setting up Airflow using Docker in the official Airflow documentation.


# Setup DinD

# Run Dags

# Security


# Acknowledgments
...


