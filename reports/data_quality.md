# Qualidade dos dados

## Verificações realizadas

A base original possui 936 linhas.

Foram identificados:

- 15 valores ausentes em `City`;
- 1 valor ausente em `Select Investors`;
- 0 duplicatas completas;
- 1 nome de empresa repetido (`Bolt`), representando empresas diferentes;
- 1 registro suspeito no campo `Company`: o valor literal `1`.

## Registro suspeito

O registro apresenta:

```text
Company: 1
Valuation: US$ 2.15 bilhões
Date Joined: 2021-09-08
Country: Brazil
City: Sao Paulo
Industry: Fintech
```

Esse registro foi **preservado** porque o projeto não corrige dados de origem sem rastreabilidade.

Fontes públicas do mesmo período apresentam **CloudWalk** com valuation de US$ 2,15 bilhões, entrada em 8 de setembro de 2021, São Paulo e setor Fintech. Isso sugere que o valor `1` pode ser um erro de captura ou transformação no arquivo fornecido.

A recomendação é manter a inconsistência documentada e só corrigi-la em uma versão futura a partir de uma fonte oficial ou versionada.

## Corte temporal

A data mais recente do arquivo fornecido é 7 de dezembro de 2021. Portanto, empresas que se tornaram unicórnios após essa data não devem ser consideradas ausentes por erro sem verificar o momento exato do snapshot.
