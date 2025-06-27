import java.util.Scanner;

public class Question2 
{

    public int[] numeros = {10,20,30};


    public static void main(String args[]) 
    {
        Scanner bola = new Scanner(System.in);
        double tempoantigo = System.currentTimeMillis();
        String s = bola.nextLine();

        if(Question2.convertime(System.currentTimeMillis() - tempoantigo) >= 2)
        {
            if (s.length() >= 5)
            {
                System.out.println(s);                
            }
            else
            {
                System.out.println("Sua Mensagem é muito Curta!");
            }
        }
        else
        {
            System.out.println("Ops, voce precisa esperar ao menos 2 segundos");
            System.out.println("Vamos tentar novamente?");
            tempoantigo = System.currentTimeMillis();
        }
        

    }

    public static double convertime(double tempo) {
        return tempo/1000;
    }
}
