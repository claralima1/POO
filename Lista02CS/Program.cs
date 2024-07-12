namespace Lista02CS;

class Program
{
    static void Main(string[] args)
    {
        Circulo c = new Circulo();
        Console.WriteLine("Digite o valor do raio: ")
        c.SetRaio(double.Parse(Console.ReadLine()));
        Console.WriteLine($" Area = {c.CalcArea()}");
        Console.WriteLine($"Circunfrencia = {c.CalcCircunferencia()}");
    }
}
