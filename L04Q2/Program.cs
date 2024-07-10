namespace L04Q2;

class Program
{
    static void Main(string[] args)
    {
        Frete f = new Frete();
        Console.WriteLine("Digite a distancia: ");
        f.set_distancia(double.Parse(Console.ReadLine()));
        Console.WriteLine("Digite o peso: ");
        f.set_peso(double.Parse(Console.ReadLine()));
        Console.WriteLine(f.ToString());
        Console.WriteLine($"Frete: {f.calc_frete()}");

    }
}
