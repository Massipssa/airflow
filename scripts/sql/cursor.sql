CREATE OR REPLACE FUNCTION my_cursor(p_year INTEGER)
    RETURN text AS $$
DECLARE
    titles TEXT  DEFAULT '';
    rec_film RECORD;
    cur_films CURSOR(p_year INTEGER)
        FOR SELECT title, release_year
        FROM fiilm
        WHERE release_year = p_year;
BEGIN
    -- Open
    OPEN cur_films(p_year);
    LOOP
        -- fetch
        FETCH cur_films INTO rec_film;
        -- exit
        EXIT WHEN NOT FOUND;

        -- build
        IF rec_film.title LIKE '%ful%' THEN
            titles := titles || ',' || rec_film.title || ':' || rec_film.release_year
         END IF;
    END LOOP;

    -- close
    CLOSE cur_films;

    RETURN titles;
END; $$

LANGUAGE plpgsql;




