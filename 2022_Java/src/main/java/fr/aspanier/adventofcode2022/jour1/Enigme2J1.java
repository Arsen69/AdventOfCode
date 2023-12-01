package fr.aspanier.adventofcode2022.jour1;

import lombok.Getter;
import lombok.Setter;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Component;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;

@Component
@Getter
@Setter
@Slf4j
public class Enigme2J1 {


    public void exec() throws IOException {

        List<String> lines = Files.readAllLines(Paths.get("C:\\Users\\Antoine\\IdeaProjects\\AdventOfCode2022\\src\\main\\resources\\Jour1\\InputPuzzle1"));
        int sum = 0;
        List<Integer> calories = new ArrayList<>();

        for (String line : lines) {
            if (line.isBlank()) {
                calories.add(sum);
                sum = 0;
                continue;
            }

            sum += Integer.parseInt(line);
        }

        calories.sort(null);

        int size = calories.size();
        log.info("La somme des trois plus grandes calories est {}", calories.get(size - 1) + calories.get(size - 2) + calories.get(size - 3));

    }
}
