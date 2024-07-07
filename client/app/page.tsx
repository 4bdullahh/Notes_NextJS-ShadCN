"use client";

import React, { useEffect, useState } from "react";

function index() {
  const [message, setMessage] = useState("loading");
  useEffect(() => {
    fetch("http://localhost:8080/api/home")
      .then((responce) => responce.json())
      .then((data) => {
        setMessage(data.message);
      });
  }, []);

  return <div>{message}</div>;
}

export default index;
