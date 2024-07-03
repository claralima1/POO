class Circulo{
    public double raio = 0;
    public double calc_area(){
        return 3.14 * this.raio **2;
    }
    public double calc_circunferencia(){
        return 2* 3.14 * this.raio;
    }
}

class MainClass {
    public static void Main (string[] args){
        Circulo x;
        x = new Circulo();
        x.raio = 10;
        Console.WriteLine("Circunferencia:")
        Console.WriteLine(x.calc_circunferencia())
        Console.WriteLine("Area: ")
        Console.WriteLine(x.calc_area())

    }
}