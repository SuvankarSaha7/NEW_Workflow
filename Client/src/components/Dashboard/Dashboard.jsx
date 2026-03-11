import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import { HashLoader } from "react-spinners";
import Division from "./Division/Division";

const Dashboard = () => {
  // const [divisions, setDivisons] = useState([]);
  const [loading, setLoading] = useState(true); // ← add this
  const [error, setError] = useState(null);

  const divisions = [
    {
      id: 1,
      division_name: "FBD",
    },
    {
      id: 2,
      division_name: "ABD",
    },
    {
      id: 3,
      division_name: "PPB",
    },
    {
      id: 4,
      division_name: "ITD",
    },
    {
      id: 5,
      division_name: "MAB",
    },
    {
      id: 6,
      division_name: "PCPB",
    },
    {
      id: 7,
      division_name: "PSPD",
    },
    {
      id: 8,
      division_name: "TM&D",
    },
    {
      id: 9,
      division_name: "ESPB",
    },
    {
      id: 10,
      division_name: "Corporate",
    },
    {
      id: 11,
      division_name: "PSPD",
    },
    {
      id: 12,
      division_name: "LSTC",
    },
  ];
  // useEffect(() => {
  //   fetch("http://127.0.0.1:8000/divisions")
  //     .then((res) => {
  //       if (res.status !== 200) throw new Error("Failed to Fetch Data");
  //       return res.json();
  //     })
  //     .then((data) => {
  //       setTimeout(() => {
  //         setDivisons(data);
  //         setLoading(false);
  //       }, 3000);
  //       console.log(data);
  //     })
  //     .catch((err) => {
  //       setTimeout(() => {
  //         setError(err.message);
  //         setLoading(false);
  //       }, 3000);
  //     });
  // }, []);

  // if (loading)
  //   return (
  //     <div className="flex justify-center items-center min-h-screen">
  //       <HashLoader />
  //     </div>
  //   );

  // if (error) return <p style={{ color: "red" }}>❌ Error: {error}</p>;

  return (
    <div className="w-full min-h-screen bg-gray-50 px-5">
      {/* Header */}
      <div className="text-center mb-12">
        <h1 className="text-xl text-gray-400 mt-1 tracking-widest uppercase">
          All Divisions
        </h1>

        <div className="mx-auto mt-2 h-1 w-16 rounded-full bg-indigo-500" />
      </div>

      {/* Division Cards Grid */}

      <div className="grid grid-cols-2 gap-10 sm:grid-cols-3 md:grid-cols-3 lg:grid-cols-3 max-w-5xl mx-auto">
        {divisions.map((division, index) => (
          <Division
            divisionName={division.division_name}
            index={index}
            key={division.id}
          />
        ))}
      </div>

      {/* Empty State */}
      {divisions.length === 0 && (
        <div className="text-center mt-20 text-gray-400">
          <p className="text-5xl mb-4">📂</p>
          <p className="text-lg font-medium">No divisions found</p>
          <p className="text-sm mt-1">Seed your database first</p>
        </div>
      )}
    </div>
  );
};

export default Dashboard;
