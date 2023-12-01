package fr.aspanier.adventofcode2022;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.scheduling.annotation.EnableScheduling;

import java.nio.file.Files;

@SpringBootApplication
@EnableScheduling
public class AdventOfCode2022Application {

    public static void main(String[] args) {
        SpringApplication.run(AdventOfCode2022Application.class, args);
    }

}
