package fr.aspanier.adventofcode2022.jour1;

import lombok.Getter;
import lombok.Setter;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Component;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;

@Component
@Getter
@Setter
@Slf4j
public class Enigme1J1 {


    public void exec() throws IOException {

        List<String> allCalories = Files.readAllLines(Paths.get("C:\\Users\\Antoine\\IdeaProjects\\AdventOfCode2022\\src\\main\\resources\\Jour1\\InputPuzzle1"));
        int maxSum = 0;
        int sum = 0;

        for (String line : allCalories) {
            if (line.isBlank()) {
                if(sum>maxSum){
                    maxSum = sum;
                }
                sum = 0;
                continue;
            }

            sum += Integer.parseInt(line);
        }

        log.info(String.valueOf(maxSum));

    }

}
