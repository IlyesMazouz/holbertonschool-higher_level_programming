-- 13-count_shows_by_genre.sql

-- This SQL script lists all genres from the 'hbtn_0d_tvshows' database and displays the number of shows linked to each
-- Each record displays: <TV Show genre> - <Number of shows linked to this genre>
-- The first column is named 'genre', and the second column is named 'number_of_shows'
-- Genres without any linked shows will not be displayed
-- Results are sorted in descending order by the number of shows linked

-- Listing genres with the number of linked shows
SELECT tv_genres.name AS genre, COUNT(tv_show_genres.genre_id) AS number_of_shows
FROM tv_genres
INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_show_genres.genre_id
ORDER BY COUNT(tv_show_genres.genre_id) DESC;
