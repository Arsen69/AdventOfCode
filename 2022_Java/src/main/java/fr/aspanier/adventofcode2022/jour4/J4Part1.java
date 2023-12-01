package fr.aspanier.adventofcode2022.jour4;

import lombok.Getter;
import lombok.Setter;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Component;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;

@Slf4j
@Component
@Getter
@Setter
public class J4Part1 {

    String path = "src\\main\\resources\\Jour4\\InputPuzzle";

    public Integer exec() throws IOException {

        List<String> lines = Files.readAllLines(Paths.get(path));

        int sum = 2;

        return sum;
    }
}
