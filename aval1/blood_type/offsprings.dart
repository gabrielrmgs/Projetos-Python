void main (){
List<String> offsprings() {
    List<String> alleles1 = ['AA', 'Ai', 'BB', 'Bi', 'AB', 'ii'];
    List<String> alleles2 = ['AA', 'Ai', 'BB', 'Bi', 'AB', 'ii'];
    List<String> rawResult = [];
    List<String> result = [];

    for (var allele1 in alleles1) {
      for (var allele2 in alleles2) {
        String offspringGenotype = allele1 + allele2;
        rawResult.add(offspringGenotype);
      }}
    for (var i in rawResult){
      if (i == "AAAA" "AAAi")
    }
    return result;}

print(offsprings());
    //return result.toSet().toList();
}
///metodo q recebe dois parametros (genotipos), dá split nos dois e concatena as primeiras partes e as segundas partes,
///se forem diferentes retorna uma lista com os dois resultados,
///se forem iguais retorna uma lista com um só elemento.