INSERT INTO genres(id, type) VALUES
  (1, 'Action'),
  (2, 'Adventure'),
  (3, 'Animated'),
  (4, 'Comedy'),
  (5, 'Drama'),
  (6, 'Fantasy'),
  (7, 'Historical'),
  (8, 'Horror'),
  (9, 'Sci-fi'),
  (10, 'Thriller'),
  (11, 'Western');

INSERT INTO movies (id, title, release_year, expiry_date) VALUES
  (1, 'Peter Rabit', 2018, '2021-06-12'),
  (2, 'The Polar Bears', 2012, '2021-06-20'),
  (3, 'Happy Feet', 2006, '2021-08-21'),
  (4, 'City Island', 2002, '2021-12-13'),
  (5, 'Me, Myself, I', 1999, '2021-10-08');

INSERT INTO movie_genres (movie_id, genre_id) VALUES
  (1, 3),
  (1, 4),
  (2, 2),
  (2, 6),
  (3, 3),
  (3, 6),
  (3, 4),
  (4, 10),
  (4, 1),
  (5, 5);