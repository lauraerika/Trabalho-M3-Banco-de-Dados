USE `unify`;

INSERT INTO `unify`.`Artista` (nome_artista, pais, streamings_mensal) VALUES
('Pink Floyd', 'Inglaterra', 245000000),
('Charli XCX', 'Inglaterra', 327000000),
('Raul Seixas', 'Brasil', 32000000),
('Linkin Park', 'Estados Unidos', 534000000);

INSERT INTO `unify`.`Genero` (nome_genero, descricao) VALUES
('Rock', 'Rock clássico, alternativo e pop rock'),
('Pop', 'Música popular comercial e hits'),
('Heavy Metal', 'Numetal e Death Metal'),
('MPB', 'Música Popular Brasileira clássica');

INSERT INTO `unify`.`Album` (nome_album, ano_lancamento, id_artista, id_genero) VALUES
('The Wall', 1979, 1, 1),
('BRAT', 2024, 2, 2),
('"Kring-Ha, Bandolo"', 1973, 3, 4),
('Meteora', 2003, 4, 3);

INSERT INTO `unify`.`Musica` (nome_musica, streamings_numero, duracao, id_album) VALUES
('Comfortably Numb', 788019458, '00:06:22', 1),
('365', 245568747, '00:03:22', 2),
('Metamorfose Ambulante', 132144934, '00:03:50', 3),
('Numb', 2514936885, '00:03:06', 4);

