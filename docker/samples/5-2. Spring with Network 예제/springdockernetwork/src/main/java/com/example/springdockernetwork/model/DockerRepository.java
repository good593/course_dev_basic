package com.example.springdockernetwork.model;

import org.springframework.data.jpa.repository.JpaRepository;

public interface DockerRepository extends JpaRepository<DockerEntity, Long> {
    
}
