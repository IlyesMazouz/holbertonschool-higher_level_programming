-- This SQL script lists all Comedy shows in the 'hbtn_0d_tvshows' database.
-- It selects show titles from the 'tv_shows' table, filtering based on the genre name "Comedy" in the 'tv_genres' table.
-- Results are sorted in ascending order by show title.

-- Listing all Comedy shows
SELECT tv_shows.title
FROM tv_shows
INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
INNER JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id
WHERE tv_genres.name = "Comedy"
ORDER BY tv_shows.title ASC;
