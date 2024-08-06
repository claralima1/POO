class Circulo {
    private double raio = 0.0;
    public Circulo()
    public void SetRaio(double r){
        if(r >=0) raio = r;
        else throw new ArgumentOutOfRangeException("informe um valor maior que 0");
    }
    public double GetRaio(){
        return raio;
    }
    public double CalcArea(){
        return 3.14 * raio *2;

    }
    public double CalcCircunferencia(){
        return 2 * 3.14 * raio;

    }
}