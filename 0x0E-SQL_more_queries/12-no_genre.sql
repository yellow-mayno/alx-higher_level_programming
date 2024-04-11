-- cross the table of shows and the table of genre
-- for each show lists the genres that the show belongs to
SELECT tv_shows.title AS title, tv_show_genres.genre_id AS genre_id FROM tv_show_genres RIGHT JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id WHERE genre_id IS NULL;
