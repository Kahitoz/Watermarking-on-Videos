import { useState } from "react";

const Video_player = () => {
  const [path, setPath] = useState("");

  const handleFilePathChange = (e) => {
    const file = e.target.files[0];
    const path = URL.createObjectURL(file);
    setPath(path);
  };


  return (
    <div>
      <div className="relative">
        <input type="file" onChange={handleFilePathChange} />
      </div>
      <div class="flex justify-center">
        <div class="w-128 h-64 relative overflow-hidden">
          {path && (
            <video class="w-full h-full object-cover" controls src={path} />
          )}
        </div>
      </div>
    </div>
  );
};
export default Video_player;
