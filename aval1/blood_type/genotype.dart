import 'dart:io';
class Genotype{
  final genotype;
  Genotype() : genotype = stdin.readLineSync() ?? 'AA';

  String bloodType(Genotype g){
    var tiruabagualado = {};
    tiruabagualado['AA'] = 'a';
    tiruabagualado['Ai'] = 'a';
    tiruabagualado['BB'] = 'b';
    tiruabagualado['Bi'] = 'b';
    tiruabagualado['AB'] = 'ab';
    tiruabagualado['ii'] = 'o'; 
    return tiruabagualado[g.genotype];
  }

  List <String> alleles (Genotype g){
    List <String> lista = [""];
    if (g == "AA"){
      lista.add("A");
    } else if (g == "Ai"){
      lista.addAll(["A","i"]);
    } else if (g == "BB"){
      lista.add("B");
    } else if (g == "Bi"){
      lista.addAll(["B","i"]);
    } else if (g == "AB"){
      lista.addAll(["A","B"]);
    } else if (g == "ii"){
      lista.add("i");} 
    return lista;
    }
  }
  var aglutinu = {'AA': ['A', 'A'], 'Ai':['A'], 'BB':['B','B'], 'Bi':['B'], 'ii':['i'], 'AB':['A','B']};
  List <String> agglutinogens (Genotype g, aglutinu){
    return aglutinu[g.genotype];
  }
  var aglutinin = {'AA': ['B'], 'Ai':['B'], 'BB':['A'], 'Bi':['A'], 'ii':['A', 'B'], 'AB':['']};
  List <String> agglutinins (Genotype g, aglutinin){
    return aglutinin[g.genotype];
  }
  var gtipos = ['AA', 'Ai', 'BB', 'Bi', 'AB', 'ii'];
  for (var gtipo in gtipos) {
    print(gtipo);
  }
  //var mapa = {'AA'};
