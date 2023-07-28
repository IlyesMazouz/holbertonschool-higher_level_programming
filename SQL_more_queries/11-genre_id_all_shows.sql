-- This SQL script lists all shows contained in the 'hbtn_0d_tvshows' database
-- Each record displays: tv_shows.title - tv_show_genres.genre_id
-- The results are sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
-- The script uses a LEFT JOIN operation to include shows even if they have no linked genres

-- Listing shows with their linked genre_ids
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;
