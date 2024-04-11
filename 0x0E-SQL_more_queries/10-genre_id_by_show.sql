-- cross the table of shows and the table of genre
-- for each show lists the genres that the show belongs to
SELECT tv_shows.title AS ttle  , tv_show_genres.genre_id AS gnre FROM tv_show_genres INNER JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id ORDER BY ttle, gnre;
