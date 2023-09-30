import Usuario from "./usuario";

export default class Aluno extends Usuario{
    public ra: string
    constructor(nome: string,ra: string){
        super(nome);
        this.ra = ra;
    }

}