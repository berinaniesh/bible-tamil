--
-- PostgreSQL database dump
--

-- Dumped from database version 15.4
-- Dumped by pg_dump version 15.4

SET client_encoding = 'UTF8';

--
-- Name: testament_type; Type: TYPE; Schema: public; Owner: berinaniesh
--

CREATE TYPE public.testament_type AS ENUM (
    'Old Testament',
    'New Testament'
);

--
-- Name: books; Type: TABLE; Schema: public; Owner: berinaniesh
--

CREATE TABLE public.books (
    id integer NOT NULL,
    name character varying NOT NULL,
    name_long character varying NOT NULL,
    name_tam character varying NOT NULL,
    name_tam_long character varying NOT NULL,
    abbreviation character varying NOT NULL,
    no_of_chapters integer DEFAULT 0 NOT NULL,
    testament public.testament_type NOT NULL,
    description text
);

--
-- Name: books_id_seq; Type: SEQUENCE; Schema: public; Owner: berinaniesh
--

CREATE SEQUENCE public.books_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.books_id_seq OWNED BY public.books.id;

--
-- Name: chapters; Type: TABLE; Schema: public; Owner: berinaniesh
--

CREATE TABLE public.chapters (
    id integer NOT NULL,
    book_id integer NOT NULL,
    chapter integer NOT NULL,
    no_of_verses integer DEFAULT 0 NOT NULL,
    description text
);


--
-- Name: chapters_id_seq; Type: SEQUENCE; Schema: public; Owner: berinaniesh
--

CREATE SEQUENCE public.chapters_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: chapters_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: berinaniesh
--

ALTER SEQUENCE public.chapters_id_seq OWNED BY public.chapters.id;

--
-- Name: verses; Type: TABLE; Schema: public; Owner: berinaniesh
--

CREATE TABLE public.verses (
    id integer NOT NULL,
    chapter_id integer NOT NULL,
    verse_number integer NOT NULL,
    verse text NOT NULL,
    description text
);


--
-- Name: verses_id_seq; Type: SEQUENCE; Schema: public; Owner: berinaniesh
--

CREATE SEQUENCE public.verses_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: verses_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: berinaniesh
--

ALTER SEQUENCE public.verses_id_seq OWNED BY public.verses.id;


--
-- Name: books id; Type: DEFAULT; Schema: public; Owner: berinaniesh
--

ALTER TABLE ONLY public.books ALTER COLUMN id SET DEFAULT nextval('public.books_id_seq'::regclass);


--
-- Name: chapters id; Type: DEFAULT; Schema: public; Owner: berinaniesh
--

ALTER TABLE ONLY public.chapters ALTER COLUMN id SET DEFAULT nextval('public.chapters_id_seq'::regclass);


--
-- Name: verses id; Type: DEFAULT; Schema: public; Owner: berinaniesh
--

ALTER TABLE ONLY public.verses ALTER COLUMN id SET DEFAULT nextval('public.verses_id_seq'::regclass);


--
-- Name: books books_abbreviation_key; Type: CONSTRAINT; Schema: public; Owner: berinaniesh
--

ALTER TABLE ONLY public.books
    ADD CONSTRAINT books_abbreviation_key UNIQUE (abbreviation);


--
-- Name: books books_name_key; Type: CONSTRAINT; Schema: public; Owner: berinaniesh
--

ALTER TABLE ONLY public.books
    ADD CONSTRAINT books_name_key UNIQUE (name);


--
-- Name: books books_pkey; Type: CONSTRAINT; Schema: public; Owner: berinaniesh
--

ALTER TABLE ONLY public.books
    ADD CONSTRAINT books_pkey PRIMARY KEY (id);


--
-- Name: chapters chapters_pkey; Type: CONSTRAINT; Schema: public; Owner: berinaniesh
--

ALTER TABLE ONLY public.chapters
    ADD CONSTRAINT chapters_pkey PRIMARY KEY (id);


--
-- Name: verses verses_pkey; Type: CONSTRAINT; Schema: public; Owner: berinaniesh
--

ALTER TABLE ONLY public.verses
    ADD CONSTRAINT verses_pkey PRIMARY KEY (id);


--
-- Name: chapters chapters_book_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: berinaniesh
--

ALTER TABLE ONLY public.chapters
    ADD CONSTRAINT chapters_book_id_fkey FOREIGN KEY (book_id) REFERENCES public.books(id) NOT VALID;


--
-- Name: verses verses_chapter_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: berinaniesh
--

ALTER TABLE ONLY public.verses
    ADD CONSTRAINT verses_chapter_id_fkey FOREIGN KEY (chapter_id) REFERENCES public.chapters(id);


--
-- PostgreSQL database dump complete
--

