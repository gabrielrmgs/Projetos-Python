class Genotype {
  final String genotype;
  final Set<String> agglutinogens;
  final Set<String> agglutinins;

  Genotype(String genotype)
      : genotype = genotype,
        agglutinogens = _calculateAgglutinogens(genotype),
        agglutinins = _calculateAgglutinins(genotype) {
    if (!["AA", "Ai", "BB", "Bi", "AB", "ii"].contains(genotype)) {
      throw Exception("Genotype inválido");
    }
  }

  String get bloodType {
    if (genotype == "AA" || genotype == "Ai") {
      return "A";
    } else if (genotype == "BB" || genotype == "Bi") {
      return "B";
    } else if (genotype == "AB") {
      return "AB";
    } else if (genotype == "ii") {
      return "O";
    } else {
      return "Desconhecido";
    }
  }

  List<String> get alleles {
    return genotype.split('').toSet().toList();
  }

  List<String> get agglutinogenss {
    return agglutinogens.toList();
  }

  List<String> get agglutininss {
    return agglutinins.toList();
  }

  List<Genotype> offsprings(Genotype other) {
    List<String> alleles1 = genotype.split('');
    List<String> alleles2 = other.genotype.split('');
    List<Genotype> result = [];

    for (var allele1 in alleles1) {
      for (var allele2 in alleles2) {
        String offspringGenotype = allele1 + allele2;
        result.add(Genotype(offspringGenotype));
      }
    }

    return result.toSet().toList();
  }

  bool compatible(Genotype other) {
    List<String> agglutinogens1 = agglutinogenss;
    List<String> agglutinogens2 = other.agglutinogenss;
    List<String> agglutinins1 = agglutininss;
    List<String> agglutinins2 = other.agglutininss;

    if (agglutinogens1.any((agglutinogen) => agglutinogens2.contains(agglutinogen)) &&
        agglutinins1.any((agglutinin) => !agglutinins2.contains(agglutinin))) {
      return true;
    }

    return false;
  }

  static Set<String> _calculateAgglutinogens(String genotype) {
    Set<String> agglutinogens = Set<String>();

    if (genotype.contains('A')) {
      agglutinogens.add('A');
    }
    if (genotype.contains('B')) {
      agglutinogens.add('B');
    }

    return agglutinogens;
  }

  static Set<String> _calculateAgglutinins(String genotype) {
    Set<String> agglutinins = Set<String>();

    if (genotype.contains('i')) {
      agglutinins.add('A');
      agglutinins.add('B');
    }

    return agglutinins;
  }
}

class Individual {
  final Genotype _genotype;
  final String _name;

  Genotype get genotype => _genotype;

  static int _autoNameCounter = 0;

  Individual(String genotype, [String? name])
      : _genotype = Genotype(genotype),
        _name = name ?? "Indiv${++_autoNameCounter}" {
    if (_autoNames.contains(_name)) {
      throw Exception("Nome duplicado");
    }
    _autoNames.add(_name);
  }

  static final Set<String> _autoNames = Set<String>();

  @override
  String toString() {
    return '$_name(${_genotype.bloodType})';
  }
}
