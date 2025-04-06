document.querySelectorAll('td').forEach(cell => {
    cell.addEventListener('mouseover', () => {
        cell.style.backgroundColor = '#d4d4d4';
    });
    cell.addEventListener('mouseout', () => {
        cell.style.backgroundColor = '';
    });
});
