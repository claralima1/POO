class Frete {
    private double distancia = 0;
    private double peso = 0;
    public Frete(){

    }
    public Frete(double d, double p){
        set_distancia(d);
        set_peso(p);
    
    }
    public void set_distancia(double d){
        if(d<=0) throw new ArgumentOutOfRangeException();
        else distancia = d;
    }

    public void set_peso(double p){
        if(p<=0) throw new ArgumentOutOfRangeException();
        else peso = p;
    }

    public double get_diatancia(){
        return distancia;
    }
    public double get_peso(){
        return peso;
    }
    public double calc_frete(){
        return 1*peso*distancia;
    }
    public override string ToString(){
        return $"Peso = {peso}, Distancia= {distancia}";
    }

}