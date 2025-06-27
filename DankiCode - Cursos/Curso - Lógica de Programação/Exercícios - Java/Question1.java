public class Question1 
{

    public int[] num = {10,20};
    public Question1() 
    {   
        int soma = 0;
        for(int i = 0; i < num.length;i++)
        {
            soma += num[i];
        }
        System.out.println(soma);
    }


    public static void main(String args[] ) 
    {
        new Question1();
    }

}
