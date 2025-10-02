import React, { useState } from "react";
import axios from "axios";
import "./App.css"; // 👈 import CSS file

function BookingForm() {
  const [form, setForm] = useState({
    no_of_adults: "1",
    no_of_children: "0",
    total_nights: "1",
    lead_time: "5",
    avg_price_per_room: "100",
    room_type_reserved: "Room_Type_1",
    type_of_meal_plan: "Meal_Plan_1",
    market_segment_type: "Online",
    repeated_guest: "No",
    no_of_special_requests: "0"
  });

  const [result, setResult] = useState("");
  const [loading, setLoading] = useState(false);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setForm({ ...form, [name]: value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setResult("");

    try {
      const payload = {
        ...form,
        no_of_adults: Number(form.no_of_adults),
        no_of_children: Number(form.no_of_children),
        total_nights: Number(form.total_nights),
        lead_time: Number(form.lead_time),
        avg_price_per_room: Number(form.avg_price_per_room),
        no_of_special_requests: Number(form.no_of_special_requests)
      };

      const apiUrl = process.env.REACT_APP_API_URL || "http://localhost:5000";
      const res = await axios.post(`${apiUrl}/predict`, payload);
      setResult(res.data.prediction);
    } catch (error) {
      console.error("Error making prediction:", error);
      setResult("⚠️ Error calling API");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="booking-container">
      <h2>Hotel Booking Prediction</h2>
      <form onSubmit={handleSubmit}>
        <label>Adults:</label>
        <input type="number" name="no_of_adults" value={form.no_of_adults} onChange={handleChange} />

        <label>Children:</label>
        <input type="number" name="no_of_children" value={form.no_of_children} onChange={handleChange} />

        <label>Total Nights:</label>
        <input type="number" name="total_nights" value={form.total_nights} onChange={handleChange} />

        <label>Lead Time (days before arrival):</label>
        <input type="number" name="lead_time" value={form.lead_time} onChange={handleChange} />

        <label>Average Price per Room:</label>
        <input type="number" name="avg_price_per_room" value={form.avg_price_per_room} onChange={handleChange} />

        <label>Room Type:</label>
        <select name="room_type_reserved" value={form.room_type_reserved} onChange={handleChange}>
          <option value="Room_Type_1">Room Type 1</option>
          <option value="Room_Type_2">Room Type 2</option>
          <option value="Room_Type_3">Room Type 3</option>
          <option value="Room_Type_4">Room Type 4</option>
        </select>

        <label>Meal Plan:</label>
        <select name="type_of_meal_plan" value={form.type_of_meal_plan} onChange={handleChange}>
          <option value="Meal_Plan_1">Meal Plan 1</option>
          <option value="Meal_Plan_2">Meal Plan 2</option>
          <option value="Meal_Plan_3">Meal Plan 3</option>
        </select>

        <label>Market Segment:</label>
        <select name="market_segment_type" value={form.market_segment_type} onChange={handleChange}>
          <option value="Online">Online</option>
          <option value="Corporate">Corporate</option>
          <option value="Offline">Offline</option>
          <option value="Complementary">Complementary</option>
        </select>

        <label>Repeated Guest:</label>
        <select name="repeated_guest" value={form.repeated_guest} onChange={handleChange}>
          <option value="No">No</option>
          <option value="Yes">Yes</option>
        </select>

        <label>Special Requests:</label>
        <input type="number" name="no_of_special_requests" value={form.no_of_special_requests} onChange={handleChange} />

        <button type="submit" disabled={loading}>
          {loading ? "Predicting..." : "Predict"}
        </button>
      </form>

      {loading && <p className="loading">⏳ Please wait, predicting...</p>}

      {result && !loading && (
        <div className={`result ${result === "Canceled" ? "danger" : "success"}`}>
          {result === "Canceled"
            ? "⚠️ High risk of cancellation. Hotel requires 30% advance payment."
            : "✅ Low risk. Booking confirmed without advance."}
        </div>
      )}
    </div>
  );
}

export default BookingForm;
