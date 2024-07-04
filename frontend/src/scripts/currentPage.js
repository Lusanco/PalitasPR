export function currentPage() {
  const pageMap = {
    "/": "Búsqueda",
    "/404": "404",
    "/about": "Acerca de Nosotros",
    "/contact": "Contáctenos",
    "/create-request": "Crear Solicitud",
    "/create-request-success": "Solicitud Creada",
    "/create-review/:id": "Crear Reseña",
    "/create-review-success": "Reseña Creada",
    "/create-service": "Crear Servicio",
    "/create-service-success": "Servicio Creado",
    "/dashboard": "Tablero",
    "/email-success": "Correo Enviado",
    "/faq": "Preguntas Frecuentes",
    "/initial-contact-success": "Contacto Inicial",
    "/login": "Iniciar Sesión",
    "/login-to-continue": "Iniciar Sesión para Continuar",
    "/logout": "Cerrar Sesión",
    "/manage-requests": "Administrar Solicitudes",
    "/manage-services": "Administrar Servicios",
    "/privacy": "Privacidad",
    "/profile/:id": "Perfil",
    "/qr": "QR",
    "/request-details/:id": "Detalles de la Solicitud",
    "/service-details/:id": "Detalles del Servicio",
    "/signup": "Registrarse",
    "/signup-success": "Registro Exitoso",
    "/tasks": "Trabajos",
    "/terms-of-use": "Términos de Uso",
    /* "test": "Prueba", */
    "*": "Not Found", // <-- Not Found

    // Add more pages here
  };

  const path = location.pathname;

  // Check for exact match first
  if (pageMap[path]) {
    return pageMap[path];
  }

  // Handle dynamic routes
  const dynamicRoutes = [
    { pattern: /^\/create-review\/[\w-]+$/, name: "Crear Reseña" },
    { pattern: /^\/request-details\/[\w-]+$/, name: "Detalles de la Solicitud" },
    { pattern: /^\/service-details\/[\w-]+$/, name: "Detalles del Servicio" },
    { pattern: /^\/profile\/[\w-]+$/, name: "Perfil" }

    // Add more dynamic routes here
  ];

  // Check for dynamic route match
  for (const route of dynamicRoutes) {
    if (route.pattern.test(path)) {
      return route.name;
    }
  }

  // Default to "Not Found" if no match is found
  return "404";
}