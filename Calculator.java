import java.util.Scanner;

public class Calculator {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Get first number from user
        System.out.print("Enter first number: ");
        double num1 = scanner.nextDouble();

        // Get second number from user
        System.out.print("Enter second number: ");
        double num2 = scanner.nextDouble();

        // Show operation menu
        System.out.println();
        System.out.println("Choose operation:");
        System.out.println("1. Addition (+)");
        System.out.println("2. Subtraction (-)");
        System.out.println("3. Multiplication (*)");
        System.out.println("4. Division (/)");
        System.out.print("Enter your choice (1-4): ");
        int choice = scanner.nextInt();

        // Perform operation using switch case
        System.out.println();
        System.out.println("=== Result ===");

        switch (choice) {
            case 1:
                System.out.printf("%.2f + %.2f = %.2f%n", num1, num2, num1 + num2);
                break;
            case 2:
                System.out.printf("%.2f - %.2f = %.2f%n", num1, num2, num1 - num2);
                break;
            case 3:
                System.out.printf("%.2f * %.2f = %.2f%n", num1, num2, num1 * num2);
                break;
            case 4:
                if (num2 != 0) {
                    System.out.printf("%.2f / %.2f = %.2f%n", num1, num2, num1 / num2);
                } else {
                    System.out.println("Error: Cannot divide by zero!");
                }
                break;
            default:
                System.out.println("Invalid choice! Please enter 1-4.");
        }

        scanner.close();
    }
}