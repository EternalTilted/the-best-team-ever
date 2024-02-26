import static org.junit.jupiter.api.Assertions.*;

class IsPrimeTest {

    @org.junit.jupiter.api.Test
    void isPrime1() {
        assertEquals(IsPrime.IsPrime(1), true);
    }
    @org.junit.jupiter.api.Test
    void isPrime2() {
        assertEquals(IsPrime.IsPrime(2), true);
    }
    @org.junit.jupiter.api.Test
    void isPrime3() {
        assertEquals(IsPrime.IsPrime(3), true);
    }
    @org.junit.jupiter.api.Test
    void isPrime4() {
        assertEquals(IsPrime.IsPrime(4), false);
    }
    @org.junit.jupiter.api.Test
    void isPrime5() {
        assertEquals(IsPrime.IsPrime(5), true);
    }
    @org.junit.jupiter.api.Test
    void isPrime6() {
        assertEquals(IsPrime.IsPrime(6), false);
    }
    @org.junit.jupiter.api.Test
    void isPrime7() {
        assertEquals(IsPrime.IsPrime(7), true);
    }
    @org.junit.jupiter.api.Test
    void isPrime8() {
        assertEquals(IsPrime.IsPrime(8), false);
    }
    @org.junit.jupiter.api.Test
    void isPrime9() {
        assertEquals(IsPrime.IsPrime(9), false);
    }
    @org.junit.jupiter.api.Test
    void isPrime10() {
        assertEquals(IsPrime.IsPrime(10), false);
    }
    @org.junit.jupiter.api.Test
    void isPrime11() {
        assertEquals(IsPrime.IsPrime(11), true);
    }
    @org.junit.jupiter.api.Test
    void isPrime12() {
        assertEquals(IsPrime.IsPrime(12), false);
    }
    @org.junit.jupiter.api.Test
    void isPrime13() {
        assertEquals(IsPrime.IsPrime(13), true);
    }
}