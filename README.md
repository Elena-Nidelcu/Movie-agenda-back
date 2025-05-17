# CineScope - Lab 7 (Back-End Integration with JWT & React)

CineScope is a movie agenda app built with React and FastAPI. It allows users to manage their watched movies, filter by various fields, and store data securely using a JWT-authenticated back-end.

---

## Technologies Used

- **Frontend:** React + Vite + Tailwind CSS
- **Backend:** FastAPI (Python)
- **Auth:** JWT with role/permission and expiration
- **API:** REST, Swagger Docs
- **Pagination:** Offset & Limit

---

## Authentication

- The app uses **JWT with role and permission**
- Token is auto-generated on app start (`role=ADMIN`, `permissions=WRITE`)
- Token expires after **1 minute**
- Protected routes: `POST`, `PUT`, `DELETE`
- Public route: `GET /movies`

---

## Features

- Add/Edit/Delete** movies (with JWT)
- Pagination with `offset` and `limit`
- Token ageneration and expiration

---

## Extra Notes

- All movie data is stored in-memory (`movies_db = []`)
- Data resets on server restart
- CORS is configured to allow front-end communication
