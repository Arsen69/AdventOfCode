package fr.aspanier.adventofcode2022.jour3;

import org.assertj.core.api.Assertions;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import java.io.IOException;

import static org.junit.jupiter.api.Assertions.*;

class Enigme2J3Test {

    static Enigme2J3 target;

    @BeforeAll
    static void init() {
        target = new Enigme2J3();
    }

    @Test
    @DisplayName("Doit bien renvoyer 18 pour r dans les 3 sacs")
    void execTestPourr() throws IOException {
        //ARRANGE

        target.setPath("src\\test\\resources\\Jour3\\First3Rucksacks");

        //ACT

        Integer result = target.exec();

        //ASSERT

        Assertions.assertThat(result).isNotNull().isEqualTo(18);
    }

    @Test
    @DisplayName("Doit bien renvoyer 52 pour Z dans les 3 sacs")
    void execTestPourZ() throws IOException {
        //ARRANGE

        target.setPath("src\\test\\resources\\Jour3\\Last3Rucksacks");

        //ACT

        Integer result = target.exec();

        //ASSERT

        Assertions.assertThat(result).isNotNull().isEqualTo(52);
    }

    @Test
    @DisplayName("Doit bien renvoyer 70 pour l'exemple")
    void execTestPourExemple() throws IOException {
        //ARRANGE

        target.setPath("src\\test\\resources\\Jour3\\AllExemple");

        //ACT

        Integer result = target.exec();

        //ASSERT

        Assertions.assertThat(result).isNotNull().isEqualTo(70);
    }
}