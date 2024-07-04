import React from 'react';

const BookingForm = ({ onTrainSearch }) => {
  return (
    <form>
      <ul>
        <b className="fsize"> From &emsp;<input type="text" placeholder="From [STN Code]" /> </b> <br /><br />
        <b className="fsize"> To &emsp;<input type="text" placeholder="To [STN Code]" /> </b> <br /><br />
        <b className="fsize"> Date &emsp;<input type="date" placeholder="dd-mm-yy" /> </b> <br /><br />
        <label className="fsize"><strong> Class </strong></label>
        <select id="class" name="class">
          <option value="select">SELECT</option>
          <option value="1AC">1AC</option>
          <option value="2AC">2AC</option>
          <option value="3AC">3AC</option>
          <option value="Sleeper">Sleeper</option>
          <option value="Chair">Chair</option>
        </select>
      </ul>
      <button className="submit" type="button" onClick={onTrainSearch}>Find Trains</button>
    </form>
  );
};

export default BookingForm;