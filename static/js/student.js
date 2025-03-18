$(document).ready(function() {
    // Initialize tooltips
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function (tooltipTriggerEl) {
      return new bootstrap.Tooltip(tooltipTriggerEl);
    });
    
    // Save event functionality
    $('.save-event').click(function() {
      const eventId = $(this).data('event-id');
      $(this).toggleClass('btn-outline-primary btn-primary');
      
      if ($(this).hasClass('btn-primary')) {
        $(this).html('<i class="bi bi-bookmark-fill"></i>');
        showToast('Event saved to your bookmarks!');
      } else {
        $(this).html('<i class="bi bi-bookmark"></i>');
        showToast('Event removed from your bookmarks.');
      }
    });
    
    // Filter events by category
    $('#categoryFilter').change(function() {
      const category = $(this).val();
      
      if (category === 'all') {
        $('#eventsContainer > div').show();
      } else {
        $('#eventsContainer > div').hide();
        $('#eventsContainer > div[data-category="' + category + '"]').show();
      }
    });
    
    // Search events
    $('#searchEvents').on('keyup', function() {
      const searchTerm = $(this).val().toLowerCase();
      
      $('#eventsContainer .card').each(function() {
        const eventText = $(this).text().toLowerCase();
        if (eventText.indexOf(searchTerm) > -1) {
          $(this).parent().show();
        } else {
          $(this).parent().hide();
        }
      });
    });
    
    // Submit event form
    $('#submitEvent').click(function() {
      // Validate form
      if ($('#createEventForm')[0].checkValidity()) {
        // Here you would typically send the form data via AJAX
        // For demonstration, we'll just show a success message
        $('#createEventModal').modal('hide');
        showToast('Event created successfully!');
        $('#createEventForm')[0].reset();
      } else {
        // Trigger browser's native validation UI
        $('#createEventForm')[0].reportValidity();
      }
    });
    
    // Function to show toast notification
    function showToast(message) {
      // Create toast container if it doesn't exist
      if (!$('#toastContainer').length) {
        $('body').append('<div id="toastContainer" class="position-fixed bottom-0 end-0 p-3" style="z-index: 11"></div>');
      }
      
      // Create toast element
      const toastId = 'toast-' + Date.now();
      const toastHtml = `
        <div id="${toastId}" class="toast" role="alert" aria-live="assertive" aria-atomic="true">
          <div class="toast-header">
            <strong class="me-auto">Notification</strong>
            <button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Close"></button>
          </div>
          <div class="toast-body">
            ${message}
          </div>
        </div>
      `;
      
      // Add toast to container
      $('#toastContainer').append(toastHtml);
      
      // Initialize and show the toast
      const toastElement = document.getElementById(toastId);
      const toast = new bootstrap.Toast(toastElement);
      toast.show();
      
      // Remove toast after it's hidden
      $(toastElement).on('hidden.bs.toast', function() {
        $(this).remove();
      });
    }
  });

  $(document).ready(function() {
    // Tab switching
    $('.tab-button').click(function() {
      $('.tab-button').removeClass('active');
      $(this).addClass('active');
      
      const tab = $(this).data('tab');
      
      if (tab === 'all') {
        $('.event-item').show();
      } else {
        $('.event-item').hide();
        $(`.event-item[data-status="${tab}"]`).show();
      }
    });
    
    // Search functionality
    $('input[type="text"]').on('keyup', function() {
      const value = $(this).val().toLowerCase();
      $('.event-item').filter(function() {
        $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1);
      });
    });
  });


  document.addEventListener('DOMContentLoaded', function() {
    // Initialize bookings array from localStorage or empty array if none exists
    let myBookings = JSON.parse(localStorage.getItem('literaryEventBookings')) || [];
    
    // Sample bookings for demonstration (remove in production)
    if (myBookings.length === 0) {
      myBookings = [
        {
          title: "Beyond the Cosmos: Interactive Workshop",
          date: "April 16, 2025 • 2:00 PM - 4:00 PM",
          location: "Science Block, Room 103"
        }
      ];
      localStorage.setItem('literaryEventBookings', JSON.stringify(myBookings));
    }
    
    // Display My Bookings
    function displayMyBookings() {
      const bookingsList = document.getElementById('bookingsList');
      const noBookings = document.getElementById('noBookings');
      const template = document.getElementById('bookingTemplate');
      
      // Clear previous bookings
      Array.from(bookingsList.children).forEach(child => {
        if (!child.id || child.id !== 'bookingTemplate') {
          bookingsList.removeChild(child);
        }
      });
      
      // Show no bookings message if there are none
      if (myBookings.length === 0) {
        noBookings.style.display = 'block';
        return;
      } else {
        noBookings.style.display = 'none';
      }
      
      // Add each booking
      myBookings.forEach((booking, index) => {
        const bookingItem = template.cloneNode(true);
        bookingItem.classList.remove('d-none');
        bookingItem.id = `booking-${index}`;
        
        bookingItem.querySelector('.booking-title').textContent = booking.title;
        bookingItem.querySelector('.booking-date').textContent = booking.date;
        bookingItem.querySelector('.booking-location').textContent = booking.location;
        
        // Add event listener for cancel button
        bookingItem.querySelector('.cancel-booking').addEventListener('click', function() {
          cancelBooking(index);
        });
        
        bookingsList.appendChild(bookingItem);
      });
    }
    
    // Cancel booking
    function cancelBooking(index) {
      if (confirm('Are you sure you want to cancel this booking?')) {
        myBookings.splice(index, 1);
        localStorage.setItem('literaryEventBookings', JSON.stringify(myBookings));
        displayMyBookings();
      }
    }
    
    // Book new session
    function bookSession(sessionName) {
      // Get session details
      const sessionElement = Array.from(document.querySelectorAll('.event-session')).find(el => {
        return el.querySelector('h5').textContent === sessionName;
      });
      
      const date = sessionElement.querySelector('.session-time').textContent;
      const location = sessionElement.querySelector('.mt-2').textContent;
      
      // Create booking object
      const newBooking = {
        title: sessionName,
        date: date,
        location: location
      };
      
      // Add to bookings
      myBookings.push(newBooking);
      localStorage.setItem('literaryEventBookings', JSON.stringify(myBookings));
      
      // Show confirmation
      const confirmationBox = document.getElementById('bookingConfirmation');
      document.getElementById('confirmationText').textContent = `You have successfully booked a seat for "${sessionName}".`;
      confirmationBox.style.display = 'block';
      
      // Scroll to confirmation
      confirmationBox.scrollIntoView({ behavior: 'smooth' });
    }
    
    // Add event listeners for booking buttons
    document.querySelectorAll('.book-btn').forEach(button => {
      button.addEventListener('click', function() {
        const sessionName = this.getAttribute('data-session');
        bookSession(sessionName);
      });
    });
    
    // Close confirmation message
    document.getElementById('closeConfirmation').addEventListener('click', function() {
      document.getElementById('bookingConfirmation').style.display = 'none';
    });
    
    // Export to calendar (simplified)
    document.getElementById('calendarExport').addEventListener('click', function() {
      alert('Calendar export feature. In a real implementation, this would generate an .ics file or integrate with Google Calendar/Outlook.');
    });
    
    // Filter sessions by search term
    document.getElementById('searchSessions').addEventListener('input', function() {
      const searchTerm = this.value.toLowerCase();
      document.querySelectorAll('.event-session').forEach(session => {
        const sessionText = session.textContent.toLowerCase();
        if (sessionText.includes(searchTerm)) {
          session.style.display = 'block';
        } else {
          session.style.display = 'none';
        }
      });
    });
    
    // Filter by day
    document.getElementById('filterByDay').addEventListener('change', function() {
      filterSessions();
    });
    
    // Filter by type
    document.getElementById('filterByType').addEventListener('change', function() {
      filterSessions();
    });
    
    // Combined filter function
    function filterSessions() {
      const dayFilter = document.getElementById('filterByDay').value;
      const typeFilter = document.getElementById('filterByType').value;
      
      document.querySelectorAll('.event-session').forEach(session => {
        const matchesDay = dayFilter === 'all' || session.getAttribute('data-date') === dayFilter;
        const matchesType = typeFilter === 'all' || session.getAttribute('data-type') === typeFilter;
        
        if (matchesDay && matchesType) {
          session.style.display = 'block';
        } else {
          session.style.display = 'none';
        }
      });
    }
    
    // Filter my bookings
    document.getElementById('filterBookings').addEventListener('input', function() {
      const searchTerm = this.value.toLowerCase();
      document.querySelectorAll('#bookingsList > div:not(#bookingTemplate)').forEach(booking => {
        const bookingText = booking.textContent.toLowerCase();
        if (bookingText.includes(searchTerm)) {
          booking.style.display = 'block';
        } else {
          booking.style.display = 'none';
        }
      });
    });
    
    // Initialize display
    displayMyBookings();
    
    // Switch to My Bookings tab if there's a hash in URL
    if (window.location.hash === '#my-bookings') {
      const myBookingsTab = new bootstrap.Tab(document.getElementById('my-bookings-tab'));
      myBookingsTab.show();
    }
  });


  document.addEventListener('DOMContentLoaded', function() {
            // Search functionality for All Clubs
            document.getElementById('clubSearch').addEventListener('input', function() {
                filterClubs('allClubsList', this.value);
            });
            
            // Search functionality for My Clubs
            document.getElementById('myClubSearch').addEventListener('input', function() {
                filterClubs('myClubsList', this.value);
            });
            
            // Category filter for All Clubs
            document.getElementById('categoryFilter').addEventListener('change', function() {
                const category = this.value;
                const cards = document.querySelectorAll('#allClubsList .club-card');
                
                cards.forEach(card => {
                    const parent = card.closest('.col-md-4');
                    const badges = card.querySelectorAll('.category-badge');
                    let matches = category === '';
                    
                    badges.forEach(badge => {
                        if (badge.textContent.toLowerCase() === category) {
                            matches = true;
                        }
                    });
                    
                    parent.style.display = matches ? '' : 'none';
                });
            });
            
            // Status filter for My Clubs
            document.getElementById('myClubStatusFilter').addEventListener('change', function() {
                const status = this.value;
                const cards = document.querySelectorAll('#myClubsList .club-card');
                
                cards.forEach(card => {
                    const parent = card.closest('.col-md-4');
                    const badge = card.querySelector('.club-badge');
                    
                    if (status === '') {
                        parent.style.display = '';
                    } else {
                        const badgeText = badge.textContent.toLowerCase();
                        parent.style.display = badgeText === status ? '' : 'none';
                    }
                });
            });
            
            // Submit new club
            document.getElementById('submitNewClub').addEventListener('click', function() {
                const form = document.getElementById('newClubForm');
                if (form.checkValidity()) {
                    alert('Club proposal submitted successfully! Your request will be reviewed by the administration.');
                    const modal = bootstrap.Modal.getInstance(document.getElementById('newClubModal'));
                    modal.hide();
                    form.reset();
                } else {
                    form.reportValidity();
                }
            });
            
            // Function to filter clubs by search text
            function filterClubs(listId, searchText) {
                const cards = document.querySelectorAll(`#${listId} .club-card`);
                const search = searchText.toLowerCase();
                
                cards.forEach(card => {
                    const parent = card.closest('.col-md-4');
                    const title = card.querySelector('.card-title').textContent.toLowerCase();
                    const description = card.querySelector('.card-text').textContent.toLowerCase();
                    const badges = Array.from(card.querySelectorAll('.category-badge')).map(b => b.textContent.toLowerCase());
                    
                    if (title.includes(search) || description.includes(search) || badges.some(b => b.includes(search))) {
                        parent.style.display = '';
                    } else {
                        parent.style.display = 'none';
                    }
                });
            }
        });