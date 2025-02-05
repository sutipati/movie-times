async function loadMovieData() {
    try {
        const response = await fetch('movie_data.json');
        const movieData = await response.json();
        
        // Update the title
        document.getElementById('movie-title').textContent = movieData.title;
        
        // Update showtimes
        const showtimesList = document.getElementById('showtimes-list');
        showtimesList.innerHTML = ''; // Clear existing items
        
        movieData.showtimes.forEach(time => {
            const li = document.createElement('li');
            li.textContent = time;
            showtimesList.appendChild(li);
        });
    } catch (error) {
        console.error('Error loading movie data:', error);
        document.getElementById('movie-title').textContent = 'Error loading movie data';
    }
}

document.addEventListener('DOMContentLoaded', loadMovieData);