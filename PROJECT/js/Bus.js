function toggleSeat(seat) {
    if (seat.classList.contains('booked')) {
        alert("This seat is already booked.");
        return;
    }

    seat.classList.toggle('selected');
}

function reserveSeats() {
    const selectedSeats = document.querySelectorAll('.seat.selected');
    if (selectedSeats.length === 0) {
        alert("No seats selected for reservation.");
        return;
    }

    selectedSeats.forEach(seat => {
        seat.classList.remove('selected');
        seat.classList.add('booked');
        seat.setAttribute('data-status', 'booked');
    });

    alert(`${selectedSeats.length} seat(s) reserved!`);
}
