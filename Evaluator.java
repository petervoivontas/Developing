import java.util.ArrayList;
import java.util.Scanner;

public class Evaluator {

    private ArrayList<String> sampleSigns = new ArrayList<>();
    private ArrayList<Float> numbers = new ArrayList<>();
    private ArrayList<String> signs = new ArrayList<>();
    private boolean isFloat;
    private float result;

    public Evaluator(String input) {
        read(input);
        eval();
    }

    public void inflateSampleSigns () {
        sampleSigns.add("+");
        sampleSigns.add("-");
        sampleSigns.add("*");
        sampleSigns.add("/");
    }

    public float add (float num1, float num2) {
        return num1 + num2;
    }

    public float subtract (float num1, float num2) {
        return num1 - num2;
    }

    public float multiply (float num1, float num2) {
        return num1 * num2;
    }

    public float divide (float num1, float num2) {
        return num1 / num2;
    }

    public void isFloat (float result) {
        boolean state = true;
        String number = String.valueOf(result);
        int dotIndex = 0;
        for (int i = 0; i < number.length(); i++) {
            if (String.valueOf(number.charAt(i)).equals(".")) {
                dotIndex = i;
            }
        }
        for (int i = dotIndex; i < number.length(); i++) {
            if (String.valueOf(number.charAt(i)).equals("0") && (i + 1) == number.length()) {
                state = false;
            } else {
                state = true;
            }
        }
        this.isFloat = state;
    }

    public void read (String input) {
        if (sampleSigns.isEmpty()) {
            inflateSampleSigns();
        }

        String expression = "";

        for (int i = 0; i < input.length(); i++) {
            Character character = input.charAt(i);

            if (Character.isDigit(character)) {
                expression += String.valueOf(character);
            } else {
                expression += " " + String.valueOf(character) + " ";
            }
        }

        for (String i:expression.split(" ")) {
            if (sampleSigns.contains(i)) {
                signs.add(i);
            } else {
                numbers.add(Float.valueOf(i));
            }
        }

        for (float i:numbers) {
            System.out.println(i);
        }

        for (String i:signs) {
            System.out.println(i);
        }

    }

    public void eval () {
        float result = 0;
        if (!((signs.contains("*") && signs.contains("/")) || signs.contains("*") || signs.contains("/"))) {
            if (signs.size() == 0) {
                result += numbers.get(0);
                this.result = result;
            } else {
                for (int i = 0; i < signs.size(); i++) {
                    String sign = signs.get(i);
                    if (sign.equals("+") && i == 0) {
                        result += add(numbers.get(i), numbers.get(i + 1));
                    } else if (sign.equals("+")) {
                        result = add(result, numbers.get(i + 1));
                    } else if (sign.equals("-") && i == 0) {
                        result += subtract(numbers.get(i), numbers.get(i + 1));
                    } else if (sign.equals("-")) {
                        result = subtract(result, numbers.get(i + 1));
                    }
                }
                this.result = result;
            }
        } else {
            removeSigns();
            eval();
        }
    }

    public void removeSigns () {
        for (int i = 0; i < signs.size(); i++) {
            String sign = signs.get(i);
            if (sign.equals("*")) {
                final float num = numbers.get(i);
                final float nextNum = numbers.get(i + 1);
                numbers.remove(i);
                numbers.remove(i);
                numbers.add(i, multiply(num, nextNum));
                signs.remove(i);
            } else if (sign.equals("/")) {
                final float num = numbers.get(i);
                final float nextNum = numbers.get(i + 1);
                numbers.remove(i);
                numbers.remove(i);
                numbers.add(i, divide(num, nextNum));
                signs.remove(i);
            }
        }
    }

    public static void main (String args[]) {
        Scanner scanner = new Scanner(System.in);
        String expression = scanner.nextLine();
        Evaluator evaluator = new Evaluator(expression);
        float result = evaluator.result;
        evaluator.isFloat(result);
        if (evaluator.isFloat) {
            System.out.println(result);
        } else {

        }
    }

}
