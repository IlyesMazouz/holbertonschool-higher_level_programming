-- This SQL script uses the 'hbtn_0d_tvshows' database to list all genres of the show "Dexter"
-- It selects genres from the 'tv_genres' table and filters based on the show "Dexter" in the 'tv_shows' table
-- Results are sorted in ascending order by genre name

-- Listing genres of the show "Dexter"
SELECT tv_genres.name
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id
WHERE tv_shows.title = "Dexter"
ORDER BY tv_genres.name ASC;
