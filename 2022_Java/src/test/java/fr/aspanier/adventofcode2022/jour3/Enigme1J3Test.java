package fr.aspanier.adventofcode2022.jour3;

import org.assertj.core.api.Assertions;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import java.io.IOException;

import static org.assertj.core.api.ClassBasedNavigableIterableAssert.assertThat;

class Enigme1J3Test {

    static Enigme1J3 target;

    @BeforeAll
    static void init() {
        target = new Enigme1J3();
    }

    @Test
    @DisplayName("Doit bien renvoyer 16 pour p identique dans les 2 compartiments")
    void execTestPourp() throws IOException {
        //ARRANGE

        target.setPath("src\\test\\resources\\Jour3\\FirstRucksack");

        //ACT

        Integer result = target.exec();

        //ASSERT

        Assertions.assertThat(result).isNotNull().isEqualTo(16);
    }

    @Test
    @DisplayName("Doit bien renvoyer 38 pour L identique dans les 2 compartiments")
    void execTestPourL() throws IOException {
        //ARRANGE

        target.setPath("src\\test\\resources\\Jour3\\SecondRucksack");

        //ACT

        Integer result = target.exec();

        //ASSERT

        Assertions.assertThat(result).isNotNull().isEqualTo(38);
    }

    @Test
    @DisplayName("Doit bien renvoyer 157 pour l'exemple")
    void execTestPourExemple() throws IOException {
        //ARRANGE

        target.setPath("src\\test\\resources\\Jour3\\AllExemple");

        //ACT

        Integer result = target.exec();

        //ASSERT

        Assertions.assertThat(result).isNotNull().isEqualTo(157);
    }
}